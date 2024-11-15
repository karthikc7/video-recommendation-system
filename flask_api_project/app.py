from flask import Flask, render_template, jsonify, abort

app = Flask(__name__)

# Sample data (replace with your actual data as needed)
video_data = [
    {"video_id": 1, "views": 100, "likes": 10, "rating": 5},
    {"video_id": 2, "views": 150, "likes": 15, "rating": 4},
    {"video_id": 3, "views": 50, "likes": 5, "rating": 3},
    {"video_id": 4, "views": 200, "likes": 20, "rating": 2},
    {"video_id": 5, "views": 250, "likes": 25, "rating": 1}
]

@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    try:
        if not video_data:
            abort(404, description="No video data available")
        recommendations = sorted(video_data, key=lambda x: x['views'], reverse=True)[:3]
        return render_template('recommendations.html', recommendations=recommendations)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Error handling for 404 errors
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

# On Vercel, we don't need app.run(debug=True) because Vercel will handle it
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


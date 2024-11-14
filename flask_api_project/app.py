from flask import Flask, jsonify, render_template, abort

app = Flask(__name__)

# Sample data (you can replace this with your actual data)
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
        # Return a sorted list of video IDs by views (top 3)
        if not video_data:
            abort(404, description="No video data available")

        recommendations = sorted(video_data, key=lambda x: x['views'], reverse=True)[:3]
        return render_template('recommendations.html', recommendations=recommendations)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

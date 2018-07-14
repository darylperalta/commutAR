using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ColorController : MonoBehaviour {

	public float c;
	const float delta = 0.15f;

	Color a;
	Color b;

	float time;
	const float period = 0.5f;

	// Use this for initialization
	void Start () {
		GetComponent<Image>().color = new Color(2f * c, 2f * (1f - c), 0f);
		InvokeRepeating("shimmer", 0f, period);
	}
	
	// Update is called once per frame
	void shimmer() {
		a = GetComponent<Image>().color;
		float x = c + Random.Range(-delta, delta);
		b = new Color(2f * x, 2f * (1f - x), 0f);
		time = Time.time;
	}

	private void Update() {
		GetComponent<Image>().color = Color.Lerp(a, b, (Time.time - time) / period);
	}
}

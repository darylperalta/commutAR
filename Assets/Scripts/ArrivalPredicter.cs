using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ArrivalPredicter : MonoBehaviour {

	public GameObject origin;
	public GameObject destination;

	Text text;

	float time;

	float rand = 0f;

	// Use this for initialization
	void Start () {
		text = GetComponent<Text>();
		InvokeRepeating("gen", 0f, 5f);
		time = Time.time;
	}
	
	// Update is called once per frame
	void Update () {
		if (origin.transform.parent.GetComponent<Button>() != null)
			if (destination.transform.parent.GetComponent<Button>() != null) {
				int steps = Mathf.Abs(destination.transform.parent.GetSiblingIndex() - origin.transform.parent.GetSiblingIndex());
				text.text = "3:";
				text.text += Mathf.RoundToInt(steps * 1.5f + 17f + rand - (Time.time - time) / 60f).ToString();
				text.text += " PM";
			}
	}

	void gen() {
		rand = Random.Range(-1f, 1f);
	}
}

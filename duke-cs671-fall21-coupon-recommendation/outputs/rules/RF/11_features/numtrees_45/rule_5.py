def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[1]<=1:
		# {"feature": "Age", "instances": 15, "metric_value": 0.8366, "depth": 2}
		if obj[3]>1:
			# {"feature": "Passanger", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[0]<=1:
				return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		elif obj[3]<=1:
			# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[7]<=1.0:
				return 'True'
			elif obj[7]>1.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[1]>1:
		return 'True'
	else: return 'True'

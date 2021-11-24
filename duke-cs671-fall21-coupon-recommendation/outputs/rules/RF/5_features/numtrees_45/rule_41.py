def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[2]>4:
		# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.3373, "depth": 2}
		if obj[3]<=2.0:
			return 'True'
		elif obj[3]>2.0:
			# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0]>1:
				return 'False'
			elif obj[0]<=1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=4:
		# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[1]<=2:
			return 'False'
		elif obj[1]>2:
			return 'True'
		else: return 'True'
	else: return 'False'

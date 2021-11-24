def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[3]<=2:
		# {"feature": "Occupation", "instances": 20, "metric_value": 1.0, "depth": 2}
		if obj[2]>1:
			# {"feature": "Coupon", "instances": 18, "metric_value": 0.9911, "depth": 3}
			if obj[0]<=3:
				# {"feature": "Education", "instances": 13, "metric_value": 0.8905, "depth": 4}
				if obj[1]<=2:
					return 'True'
				elif obj[1]>2:
					return 'False'
				else: return 'False'
			elif obj[0]>3:
				# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[1]>0:
					return 'False'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]<=1:
			return 'False'
		else: return 'False'
	elif obj[3]>2:
		return 'False'
	else: return 'False'

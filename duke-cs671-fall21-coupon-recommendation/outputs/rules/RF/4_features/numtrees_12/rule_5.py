def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9975, "depth": 1}
	if obj[0]>0:
		# {"feature": "Occupation", "instances": 70, "metric_value": 0.9518, "depth": 2}
		if obj[2]>0:
			# {"feature": "Distance", "instances": 68, "metric_value": 0.9597, "depth": 3}
			if obj[3]<=2:
				# {"feature": "Education", "instances": 59, "metric_value": 0.9393, "depth": 4}
				if obj[1]<=4:
					return 'True'
				elif obj[1]>4:
					return 'True'
				else: return 'True'
			elif obj[3]>2:
				# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[2]<=0:
			return 'True'
		else: return 'True'
	elif obj[0]<=0:
		# {"feature": "Occupation", "instances": 15, "metric_value": 0.3534, "depth": 2}
		if obj[2]<=7:
			return 'False'
		elif obj[2]>7:
			# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'

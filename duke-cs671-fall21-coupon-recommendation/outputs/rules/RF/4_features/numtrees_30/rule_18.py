def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Distance", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[3]<=2:
		# {"feature": "Occupation", "instances": 31, "metric_value": 0.9812, "depth": 2}
		if obj[2]<=7:
			# {"feature": "Coupon", "instances": 18, "metric_value": 0.8524, "depth": 3}
			if obj[0]>0:
				# {"feature": "Education", "instances": 14, "metric_value": 0.5917, "depth": 4}
				if obj[1]<=2:
					return 'True'
				elif obj[1]>2:
					return 'True'
				else: return 'True'
			elif obj[0]<=0:
				# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[1]<=0:
					return 'False'
				elif obj[1]>0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[2]>7:
			# {"feature": "Coupon", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[0]<=3:
				# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			elif obj[0]>3:
				# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[1]<=1:
					return 'False'
				elif obj[1]>1:
					return 'False'
				else: return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[3]>2:
		return 'False'
	else: return 'False'

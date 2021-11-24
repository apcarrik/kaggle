def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[0]<=3:
		# {"feature": "Occupation", "instances": 25, "metric_value": 0.9988, "depth": 2}
		if obj[2]>0:
			# {"feature": "Restaurant20to50", "instances": 24, "metric_value": 0.995, "depth": 3}
			if obj[3]>0.0:
				# {"feature": "Distance", "instances": 23, "metric_value": 0.9877, "depth": 4}
				if obj[4]<=2:
					# {"feature": "Education", "instances": 22, "metric_value": 0.994, "depth": 5}
					if obj[1]>1:
						return 'False'
					elif obj[1]<=1:
						return 'True'
					else: return 'True'
				elif obj[4]>2:
					return 'False'
				else: return 'False'
			elif obj[3]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[2]<=0:
			return 'True'
		else: return 'True'
	elif obj[0]>3:
		# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[2]<=5:
			return 'True'
		elif obj[2]>5:
			# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[3]<=1.0:
				return 'True'
			elif obj[3]>1.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'

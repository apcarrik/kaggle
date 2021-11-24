def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[0]>0:
		# {"feature": "Occupation", "instances": 29, "metric_value": 0.9923, "depth": 2}
		if obj[2]>2:
			# {"feature": "Distance", "instances": 25, "metric_value": 0.9988, "depth": 3}
			if obj[4]<=2:
				# {"feature": "Education", "instances": 21, "metric_value": 0.9587, "depth": 4}
				if obj[1]>0:
					# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[3]<=2.0:
						return 'False'
					elif obj[3]>2.0:
						return 'True'
					else: return 'True'
				elif obj[1]<=0:
					# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[3]<=1.0:
						return 'True'
					elif obj[3]>1.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[4]>2:
				return 'False'
			else: return 'False'
		elif obj[2]<=2:
			return 'False'
		else: return 'False'
	elif obj[0]<=0:
		return 'False'
	else: return 'False'

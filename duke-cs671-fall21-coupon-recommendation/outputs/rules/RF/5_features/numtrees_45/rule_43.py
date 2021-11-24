def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[0]>0:
		# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.8315, "depth": 2}
		if obj[3]<=2.0:
			# {"feature": "Occupation", "instances": 18, "metric_value": 0.7642, "depth": 3}
			if obj[2]<=12:
				# {"feature": "Education", "instances": 16, "metric_value": 0.8113, "depth": 4}
				if obj[1]>1:
					# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=2:
						return 'True'
					elif obj[4]>2:
						return 'True'
					else: return 'True'
				elif obj[1]<=1:
					# {"feature": "Distance", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[4]<=2:
						return 'True'
					elif obj[4]>2:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[2]>12:
				return 'True'
			else: return 'True'
		elif obj[3]>2.0:
			return 'False'
		else: return 'False'
	elif obj[0]<=0:
		# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 2}
		if obj[1]>0:
			return 'False'
		elif obj[1]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'

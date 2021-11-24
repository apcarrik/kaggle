def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[0]>0:
		# {"feature": "Occupation", "instances": 44, "metric_value": 0.9457, "depth": 2}
		if obj[2]<=14:
			# {"feature": "Education", "instances": 39, "metric_value": 0.9766, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Distance", "instances": 36, "metric_value": 0.9911, "depth": 4}
				if obj[4]<=2:
					# {"feature": "Restaurant20to50", "instances": 27, "metric_value": 0.999, "depth": 5}
					if obj[3]<=1.0:
						return 'True'
					elif obj[3]>1.0:
						return 'False'
					else: return 'False'
				elif obj[4]>2:
					# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[3]>0.0:
						return 'True'
					elif obj[3]<=0.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[2]>14:
			return 'True'
		else: return 'True'
	elif obj[0]<=0:
		# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[1]<=3:
			return 'False'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	else: return 'False'

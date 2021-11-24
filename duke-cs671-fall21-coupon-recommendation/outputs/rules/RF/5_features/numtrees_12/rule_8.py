def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Education", "instances": 85, "metric_value": 0.9919, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Occupation", "instances": 77, "metric_value": 0.9989, "depth": 2}
		if obj[2]<=21:
			# {"feature": "Distance", "instances": 74, "metric_value": 1.0, "depth": 3}
			if obj[4]>1:
				# {"feature": "Coupon", "instances": 43, "metric_value": 0.9682, "depth": 4}
				if obj[0]>0:
					# {"feature": "Restaurant20to50", "instances": 33, "metric_value": 0.9993, "depth": 5}
					if obj[3]<=1.0:
						return 'False'
					elif obj[3]>1.0:
						return 'True'
					else: return 'True'
				elif obj[0]<=0:
					# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.469, "depth": 5}
					if obj[3]<=1.0:
						return 'False'
					elif obj[3]>1.0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[4]<=1:
				# {"feature": "Restaurant20to50", "instances": 31, "metric_value": 0.9383, "depth": 4}
				if obj[3]>0.0:
					# {"feature": "Coupon", "instances": 27, "metric_value": 0.9751, "depth": 5}
					if obj[0]>1:
						return 'True'
					elif obj[0]<=1:
						return 'True'
					else: return 'True'
				elif obj[3]<=0.0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[2]>21:
			return 'True'
		else: return 'True'
	elif obj[1]>3:
		# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 2}
		if obj[0]<=3:
			return 'True'
		elif obj[0]>3:
			# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[3]>0.0:
				return 'False'
			elif obj[3]<=0.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'

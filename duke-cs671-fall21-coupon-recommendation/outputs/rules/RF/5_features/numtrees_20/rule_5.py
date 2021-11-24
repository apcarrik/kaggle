def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[2]<=17:
		# {"feature": "Restaurant20to50", "instances": 46, "metric_value": 1.0, "depth": 2}
		if obj[3]<=1.0:
			# {"feature": "Distance", "instances": 31, "metric_value": 0.9383, "depth": 3}
			if obj[4]<=2:
				# {"feature": "Coupon", "instances": 27, "metric_value": 0.8767, "depth": 4}
				if obj[0]>0:
					# {"feature": "Education", "instances": 21, "metric_value": 0.9183, "depth": 5}
					if obj[1]>0:
						return 'False'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				elif obj[0]<=0:
					# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[1]>0:
						return 'False'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[4]>2:
				# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[0]>0:
					return 'True'
				elif obj[0]<=0:
					# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]<=0:
						return 'False'
					else: return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[3]>1.0:
			# {"feature": "Distance", "instances": 15, "metric_value": 0.7219, "depth": 3}
			if obj[4]<=2:
				# {"feature": "Education", "instances": 13, "metric_value": 0.3912, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[0]>1:
						return 'True'
					elif obj[0]<=1:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[4]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[2]>17:
		return 'True'
	else: return 'True'

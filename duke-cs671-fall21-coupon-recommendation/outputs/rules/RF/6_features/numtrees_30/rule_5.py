def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[2]<=2:
		# {"feature": "Passanger", "instances": 23, "metric_value": 0.8865, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Occupation", "instances": 17, "metric_value": 0.9774, "depth": 3}
			if obj[3]>2:
				# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 1.0, "depth": 4}
				if obj[4]<=1.0:
					# {"feature": "Distance", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[5]<=2:
						# {"feature": "Coupon", "instances": 11, "metric_value": 0.9457, "depth": 6}
						if obj[1]<=3:
							return 'False'
						elif obj[1]>3:
							return 'False'
						else: return 'False'
					elif obj[5]>2:
						return 'True'
					else: return 'True'
				elif obj[4]>1.0:
					return 'True'
				else: return 'True'
			elif obj[3]<=2:
				return 'True'
			else: return 'True'
		elif obj[0]>2:
			return 'True'
		else: return 'True'
	elif obj[2]>2:
		# {"feature": "Occupation", "instances": 11, "metric_value": 0.8454, "depth": 2}
		if obj[3]>4:
			# {"feature": "Coupon", "instances": 10, "metric_value": 0.7219, "depth": 3}
			if obj[1]>2:
				# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[4]<=1.0:
						return 'False'
					elif obj[4]>1.0:
						# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]<=1:
							return 'False'
						elif obj[5]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[1]<=2:
				return 'False'
			else: return 'False'
		elif obj[3]<=4:
			return 'True'
		else: return 'True'
	else: return 'False'

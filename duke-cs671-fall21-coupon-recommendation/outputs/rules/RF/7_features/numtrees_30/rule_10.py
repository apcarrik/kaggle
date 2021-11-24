def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[2]<=1:
		# {"feature": "Coupon", "instances": 18, "metric_value": 0.7642, "depth": 2}
		if obj[1]>2:
			# {"feature": "Passanger", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Occupation", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[3]<=2:
					# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[5]<=0:
						# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[6]<=1:
							# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4]<=1.0:
								return 'False'
							else: return 'False'
						elif obj[6]>1:
							return 'False'
						else: return 'False'
					elif obj[5]>0:
						return 'True'
					else: return 'True'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		elif obj[1]<=2:
			return 'False'
		else: return 'False'
	elif obj[2]>1:
		# {"feature": "Distance", "instances": 16, "metric_value": 0.6962, "depth": 2}
		if obj[6]>1:
			# {"feature": "Passanger", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[0]>0:
				# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[4]<=1.0:
					# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[3]>1:
						# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[1]>2:
							return 'True'
						elif obj[1]<=2:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[3]<=1:
						return 'False'
					else: return 'False'
				elif obj[4]>1.0:
					return 'True'
				else: return 'True'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		elif obj[6]<=1:
			return 'True'
		else: return 'True'
	else: return 'True'

def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Bar", "instances": 34, "metric_value": 0.8338, "depth": 1}
	if obj[4]<=1.0:
		# {"feature": "Occupation", "instances": 26, "metric_value": 0.9306, "depth": 2}
		if obj[3]<=11:
			# {"feature": "Direction_same", "instances": 23, "metric_value": 0.8281, "depth": 3}
			if obj[6]<=0:
				# {"feature": "Education", "instances": 21, "metric_value": 0.7025, "depth": 4}
				if obj[2]<=1:
					return 'True'
				elif obj[2]>1:
					# {"feature": "Coupon", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[1]>0:
						# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[5]<=1.0:
							# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[7]<=2:
								# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[0]>1:
									return 'False'
								elif obj[0]<=1:
									return 'True'
								else: return 'True'
							elif obj[7]>2:
								return 'False'
							else: return 'False'
						elif obj[5]>1.0:
							return 'True'
						else: return 'True'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[6]>0:
				return 'False'
			else: return 'False'
		elif obj[3]>11:
			return 'False'
		else: return 'False'
	elif obj[4]>1.0:
		return 'True'
	else: return 'True'

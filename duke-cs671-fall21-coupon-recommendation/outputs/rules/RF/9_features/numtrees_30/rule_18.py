def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Bar", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[5]<=1.0:
		# {"feature": "Occupation", "instances": 24, "metric_value": 0.9544, "depth": 2}
		if obj[4]<=8:
			# {"feature": "Coupon", "instances": 19, "metric_value": 0.998, "depth": 3}
			if obj[2]>0:
				# {"feature": "Distance", "instances": 16, "metric_value": 0.9887, "depth": 4}
				if obj[8]>1:
					# {"feature": "Time", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[1]>0:
						# {"feature": "Education", "instances": 11, "metric_value": 0.9457, "depth": 6}
						if obj[3]>0:
							# {"feature": "Passanger", "instances": 8, "metric_value": 1.0, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[6]<=2.0:
									# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=0:
										return 'False'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								elif obj[6]>2.0:
									return 'True'
								else: return 'True'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						elif obj[3]<=0:
							return 'False'
						else: return 'False'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				elif obj[8]<=1:
					return 'True'
				else: return 'True'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		elif obj[4]>8:
			return 'False'
		else: return 'False'
	elif obj[5]>1.0:
		# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[6]<=2.0:
			return 'True'
		elif obj[6]>2.0:
			# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0]<=2:
				return 'False'
			elif obj[0]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'

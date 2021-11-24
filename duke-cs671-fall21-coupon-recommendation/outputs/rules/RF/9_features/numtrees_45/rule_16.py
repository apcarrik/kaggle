def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Occupation", "instances": 12, "metric_value": 0.9183, "depth": 2}
		if obj[4]<=12:
			# {"feature": "Bar", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[5]<=2.0:
				# {"feature": "Time", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[3]<=0:
						# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]<=0:
							# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]<=1.0:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]<=3:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[2]>0:
							return 'False'
						else: return 'False'
					elif obj[3]>0:
						return 'True'
					else: return 'True'
				elif obj[1]>2:
					return 'False'
				else: return 'False'
			elif obj[5]>2.0:
				return 'True'
			else: return 'True'
		elif obj[4]>12:
			return 'False'
		else: return 'False'
	elif obj[0]>2:
		# {"feature": "Education", "instances": 11, "metric_value": 0.684, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Bar", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[5]>-1.0:
				return 'True'
			elif obj[5]<=-1.0:
				return 'False'
			else: return 'False'
		elif obj[3]>2:
			return 'False'
		else: return 'False'
	else: return 'True'

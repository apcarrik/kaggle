def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[4]<=14:
		# {"feature": "Coupon", "instances": 31, "metric_value": 0.8691, "depth": 2}
		if obj[2]>0:
			# {"feature": "Time", "instances": 29, "metric_value": 0.7973, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Bar", "instances": 24, "metric_value": 0.8709, "depth": 4}
				if obj[5]<=3.0:
					# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.8281, "depth": 5}
					if obj[6]<=2.0:
						# {"feature": "Education", "instances": 16, "metric_value": 0.9544, "depth": 6}
						if obj[3]<=3:
							# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9957, "depth": 7}
							if obj[7]<=2.0:
								# {"feature": "Passanger", "instances": 11, "metric_value": 0.994, "depth": 8}
								if obj[0]<=2:
									# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 9}
									if obj[9]<=1:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[8]>0:
											return 'False'
										elif obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[9]>1:
										return 'False'
									else: return 'False'
								elif obj[0]>2:
									# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[9]<=1:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[9]>1:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[7]>2.0:
								return 'True'
							else: return 'True'
						elif obj[3]>3:
							return 'True'
						else: return 'True'
					elif obj[6]>2.0:
						return 'True'
					else: return 'True'
				elif obj[5]>3.0:
					return 'False'
				else: return 'False'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[2]<=0:
			return 'False'
		else: return 'False'
	elif obj[4]>14:
		return 'False'
	else: return 'False'

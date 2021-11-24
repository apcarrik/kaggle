def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Bar", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[5]<=1.0:
		# {"feature": "Occupation", "instances": 18, "metric_value": 0.9911, "depth": 2}
		if obj[4]>4:
			# {"feature": "Passanger", "instances": 15, "metric_value": 0.9183, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Time", "instances": 10, "metric_value": 1.0, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[3]<=2:
						return 'True'
					elif obj[3]>2:
						# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]>0:
							# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]<=1.0:
								# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=2.0:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]<=1:
										# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[9]<=1:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[2]<=0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[1]>2:
					return 'False'
				else: return 'False'
			elif obj[0]>2:
				return 'True'
			else: return 'True'
		elif obj[4]<=4:
			return 'False'
		else: return 'False'
	elif obj[5]>1.0:
		return 'True'
	else: return 'True'

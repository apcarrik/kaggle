def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[4]<=16:
		# {"feature": "Passanger", "instances": 49, "metric_value": 0.9486, "depth": 2}
		if obj[0]>0:
			# {"feature": "Time", "instances": 44, "metric_value": 0.976, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Bar", "instances": 33, "metric_value": 0.9993, "depth": 4}
				if obj[5]<=2.0:
					# {"feature": "Restaurant20to50", "instances": 30, "metric_value": 0.9968, "depth": 5}
					if obj[7]>-1.0:
						# {"feature": "Coupon", "instances": 29, "metric_value": 0.9923, "depth": 6}
						if obj[2]>0:
							# {"feature": "Education", "instances": 27, "metric_value": 0.999, "depth": 7}
							if obj[3]>1:
								# {"feature": "Distance", "instances": 15, "metric_value": 0.971, "depth": 8}
								if obj[9]<=2:
									# {"feature": "Coffeehouse", "instances": 14, "metric_value": 0.9403, "depth": 9}
									if obj[6]<=3.0:
										# {"feature": "Direction_same", "instances": 13, "metric_value": 0.9612, "depth": 10}
										if obj[8]<=0:
											return 'True'
										elif obj[8]>0:
											return 'True'
										else: return 'True'
									elif obj[6]>3.0:
										return 'True'
									else: return 'True'
								elif obj[9]>2:
									return 'False'
								else: return 'False'
							elif obj[3]<=1:
								# {"feature": "Direction_same", "instances": 12, "metric_value": 0.9183, "depth": 8}
								if obj[8]<=0:
									# {"feature": "Distance", "instances": 11, "metric_value": 0.8454, "depth": 9}
									if obj[9]<=2:
										# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.7219, "depth": 10}
										if obj[6]>0.0:
											return 'False'
										elif obj[6]<=0.0:
											return 'False'
										else: return 'False'
									elif obj[9]>2:
										return 'True'
									else: return 'True'
								elif obj[8]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[2]<=0:
							return 'False'
						else: return 'False'
					elif obj[7]<=-1.0:
						return 'True'
					else: return 'True'
				elif obj[5]>2.0:
					return 'True'
				else: return 'True'
			elif obj[1]>3:
				# {"feature": "Education", "instances": 11, "metric_value": 0.684, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=3:
						return 'False'
					elif obj[2]>3:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	elif obj[4]>16:
		return 'False'
	else: return 'False'

def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[2]>0:
		# {"feature": "Time", "instances": 29, "metric_value": 0.9576, "depth": 2}
		if obj[1]>0:
			# {"feature": "Education", "instances": 24, "metric_value": 0.995, "depth": 3}
			if obj[4]<=2:
				# {"feature": "Occupation", "instances": 20, "metric_value": 0.9928, "depth": 4}
				if obj[5]<=12:
					# {"feature": "Age", "instances": 15, "metric_value": 0.9968, "depth": 5}
					if obj[3]<=4:
						# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9957, "depth": 6}
						if obj[8]<=1.0:
							# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[7]<=2.0:
								# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[6]<=1.0:
										# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[10]>1:
											return 'False'
										elif obj[10]<=1:
											return 'True'
										else: return 'True'
									elif obj[6]>1.0:
										return 'True'
									else: return 'True'
								elif obj[0]>1:
									return 'False'
								else: return 'False'
							elif obj[7]>2.0:
								return 'True'
							else: return 'True'
						elif obj[8]>1.0:
							# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[0]<=2:
								return 'False'
							elif obj[0]>2:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[3]>4:
						return 'True'
					else: return 'True'
				elif obj[5]>12:
					# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[3]>1:
						return 'False'
					elif obj[3]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]>2:
				return 'True'
			else: return 'True'
		elif obj[1]<=0:
			return 'True'
		else: return 'True'
	elif obj[2]<=0:
		return 'False'
	else: return 'False'

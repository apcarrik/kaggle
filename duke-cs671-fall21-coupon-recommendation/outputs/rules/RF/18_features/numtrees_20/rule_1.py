def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Education", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[9]<=2:
		# {"feature": "Occupation", "instances": 41, "metric_value": 0.9789, "depth": 2}
		if obj[10]>1:
			# {"feature": "Age", "instances": 37, "metric_value": 0.9353, "depth": 3}
			if obj[6]>0:
				# {"feature": "Passanger", "instances": 33, "metric_value": 0.885, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Income", "instances": 28, "metric_value": 0.9403, "depth": 5}
					if obj[11]>1:
						# {"feature": "Children", "instances": 24, "metric_value": 0.8709, "depth": 6}
						if obj[8]<=0:
							# {"feature": "Restaurantlessthan20", "instances": 13, "metric_value": 0.9957, "depth": 7}
							if obj[14]<=2.0:
								# {"feature": "Coupon_validity", "instances": 10, "metric_value": 0.971, "depth": 8}
								if obj[4]>0:
									# {"feature": "Maritalstatus", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[7]<=1:
										return 'False'
									elif obj[7]>1:
										# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[2]>0:
											return 'True'
										elif obj[2]<=0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[4]<=0:
									# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[15]>-1.0:
										return 'True'
									elif obj[15]<=-1.0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[14]>2.0:
								return 'True'
							else: return 'True'
						elif obj[8]>0:
							# {"feature": "Coupon", "instances": 11, "metric_value": 0.4395, "depth": 7}
							if obj[3]>1:
								return 'True'
							elif obj[3]<=1:
								# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[1]>0:
									return 'True'
								elif obj[1]<=0:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[11]<=1:
						# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[1]>0:
							return 'False'
						elif obj[1]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[0]>2:
					return 'True'
				else: return 'True'
			elif obj[6]<=0:
				# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[1]<=0:
					return 'False'
				elif obj[1]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[10]<=1:
			return 'False'
		else: return 'False'
	elif obj[9]>2:
		# {"feature": "Restaurantlessthan20", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[14]>1.0:
			return 'False'
		elif obj[14]<=1.0:
			return 'True'
		else: return 'True'
	else: return 'False'

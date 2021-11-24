def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Direction_same", "instances": 51, "metric_value": 0.9367, "depth": 1}
	if obj[17]<=0:
		# {"feature": "Restaurantlessthan20", "instances": 46, "metric_value": 0.9656, "depth": 2}
		if obj[15]<=3.0:
			# {"feature": "Education", "instances": 42, "metric_value": 0.9852, "depth": 3}
			if obj[10]>0:
				# {"feature": "Weather", "instances": 26, "metric_value": 0.9957, "depth": 4}
				if obj[1]<=0:
					# {"feature": "Income", "instances": 22, "metric_value": 0.994, "depth": 5}
					if obj[12]<=6:
						# {"feature": "Coupon", "instances": 20, "metric_value": 0.971, "depth": 6}
						if obj[4]>3:
							# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9957, "depth": 7}
							if obj[16]>-1.0:
								# {"feature": "Passanger", "instances": 12, "metric_value": 0.9799, "depth": 8}
								if obj[0]>1:
									# {"feature": "Gender", "instances": 7, "metric_value": 0.9852, "depth": 9}
									if obj[6]<=0:
										# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[2]<=55:
											return 'False'
										elif obj[2]>55:
											# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[5]<=0:
												return 'True'
											elif obj[5]>0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[6]>0:
										return 'True'
									else: return 'True'
								elif obj[0]<=1:
									# {"feature": "Coupon_validity", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[5]<=0:
										# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[7]>1:
											return 'False'
										elif obj[7]<=1:
											return 'True'
										else: return 'True'
									elif obj[5]>0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[16]<=-1.0:
								return 'True'
							else: return 'True'
						elif obj[4]<=3:
							# {"feature": "Age", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[7]>0:
								return 'True'
							elif obj[7]<=0:
								# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[0]<=2:
									return 'False'
								elif obj[0]>2:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					elif obj[12]>6:
						return 'False'
					else: return 'False'
				elif obj[1]>0:
					return 'False'
				else: return 'False'
			elif obj[10]<=0:
				# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.8113, "depth": 4}
				if obj[14]>0.0:
					# {"feature": "Time", "instances": 14, "metric_value": 0.5917, "depth": 5}
					if obj[3]>1:
						return 'True'
					elif obj[3]<=1:
						# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[7]>3:
							return 'True'
						elif obj[7]<=3:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[14]<=0.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[15]>3.0:
			return 'True'
		else: return 'True'
	elif obj[17]>0:
		return 'True'
	else: return 'True'

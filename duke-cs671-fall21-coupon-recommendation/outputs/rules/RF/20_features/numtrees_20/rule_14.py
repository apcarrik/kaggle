def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Bar", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[14]<=2.0:
		# {"feature": "Income", "instances": 44, "metric_value": 0.9985, "depth": 2}
		if obj[13]>1:
			# {"feature": "Occupation", "instances": 36, "metric_value": 0.9641, "depth": 3}
			if obj[12]<=10:
				# {"feature": "Education", "instances": 29, "metric_value": 0.9991, "depth": 4}
				if obj[11]<=2:
					# {"feature": "Coupon", "instances": 25, "metric_value": 0.9896, "depth": 5}
					if obj[5]>1:
						# {"feature": "Age", "instances": 16, "metric_value": 0.8113, "depth": 6}
						if obj[8]<=2:
							# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[17]>0.0:
								# {"feature": "Driving_to", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Maritalstatus", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[9]>0:
										return 'False'
									elif obj[9]<=0:
										# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[15]<=1.0:
											return 'True'
										elif obj[15]>1.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[0]>1:
									return 'True'
								else: return 'True'
							elif obj[17]<=0.0:
								return 'True'
							else: return 'True'
						elif obj[8]>2:
							return 'True'
						else: return 'True'
					elif obj[5]<=1:
						# {"feature": "Weather", "instances": 9, "metric_value": 0.7642, "depth": 6}
						if obj[2]<=1:
							return 'False'
						elif obj[2]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[11]>2:
					return 'False'
				else: return 'False'
			elif obj[12]>10:
				return 'False'
			else: return 'False'
		elif obj[13]<=1:
			# {"feature": "Passanger", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[1]<=2:
				return 'True'
			elif obj[1]>2:
				# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=55:
					return 'True'
				elif obj[3]>55:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[14]>2.0:
		return 'True'
	else: return 'True'

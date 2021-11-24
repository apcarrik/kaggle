def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[12]>1:
		# {"feature": "Coffeehouse", "instances": 43, "metric_value": 0.9808, "depth": 2}
		if obj[15]<=3.0:
			# {"feature": "Age", "instances": 37, "metric_value": 0.9995, "depth": 3}
			if obj[8]<=6:
				# {"feature": "Education", "instances": 34, "metric_value": 0.9975, "depth": 4}
				if obj[11]>0:
					# {"feature": "Weather", "instances": 22, "metric_value": 0.976, "depth": 5}
					if obj[2]<=0:
						# {"feature": "Time", "instances": 18, "metric_value": 1.0, "depth": 6}
						if obj[4]<=2:
							# {"feature": "Income", "instances": 12, "metric_value": 0.9183, "depth": 7}
							if obj[13]<=3:
								# {"feature": "Bar", "instances": 9, "metric_value": 0.9911, "depth": 8}
								if obj[14]>0.0:
									# {"feature": "Gender", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[7]>0:
										return 'True'
									elif obj[7]<=0:
										return 'False'
									else: return 'False'
								elif obj[14]<=0.0:
									# {"feature": "Driving_to", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[0]<=1:
										return 'False'
									elif obj[0]>1:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[13]>3:
								return 'True'
							else: return 'True'
						elif obj[4]>2:
							# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[7]>0:
								return 'False'
							elif obj[7]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[2]>0:
						return 'False'
					else: return 'False'
				elif obj[11]<=0:
					# {"feature": "Coupon", "instances": 12, "metric_value": 0.8113, "depth": 5}
					if obj[5]<=2:
						return 'True'
					elif obj[5]>2:
						# {"feature": "Maritalstatus", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[9]<=1:
							# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[2]<=0:
								return 'True'
							elif obj[2]>0:
								return 'False'
							else: return 'False'
						elif obj[9]>1:
							return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[8]>6:
				return 'False'
			else: return 'False'
		elif obj[15]>3.0:
			return 'False'
		else: return 'False'
	elif obj[12]<=1:
		# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 2}
		if obj[5]>0:
			return 'True'
		elif obj[5]<=0:
			# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0]>0:
				return 'False'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'

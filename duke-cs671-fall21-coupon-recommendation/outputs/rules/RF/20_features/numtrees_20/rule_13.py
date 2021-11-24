def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Bar", "instances": 51, "metric_value": 0.9183, "depth": 1}
	if obj[14]<=1.0:
		# {"feature": "Passanger", "instances": 39, "metric_value": 0.9881, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Income", "instances": 28, "metric_value": 0.9852, "depth": 3}
			if obj[13]<=5:
				# {"feature": "Restaurantlessthan20", "instances": 19, "metric_value": 0.8315, "depth": 4}
				if obj[16]<=2.0:
					# {"feature": "Coupon_validity", "instances": 13, "metric_value": 0.9612, "depth": 5}
					if obj[6]<=0:
						# {"feature": "Driving_to", "instances": 10, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Age", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[8]<=6:
								# {"feature": "Occupation", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[12]>2:
									# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[15]>-1.0:
										return 'True'
									elif obj[15]<=-1.0:
										return 'False'
									else: return 'False'
								elif obj[12]<=2:
									return 'False'
								else: return 'False'
							elif obj[8]>6:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					elif obj[6]>0:
						return 'False'
					else: return 'False'
				elif obj[16]>2.0:
					return 'False'
				else: return 'False'
			elif obj[13]>5:
				# {"feature": "Driving_to", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[0]<=1:
					return 'True'
				elif obj[0]>1:
					# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=0:
						return 'False'
					elif obj[2]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[1]>2:
			# {"feature": "Age", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[8]>0:
				return 'True'
			elif obj[8]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[14]>1.0:
		return 'True'
	else: return 'True'

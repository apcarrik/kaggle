def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Restaurantlessthan20", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[16]>1.0:
		# {"feature": "Weather", "instances": 19, "metric_value": 0.9495, "depth": 2}
		if obj[2]<=1:
			# {"feature": "Maritalstatus", "instances": 18, "metric_value": 0.9183, "depth": 3}
			if obj[9]<=1:
				# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.874, "depth": 4}
				if obj[15]<=2.0:
					# {"feature": "Temperature", "instances": 13, "metric_value": 0.9612, "depth": 5}
					if obj[3]>55:
						# {"feature": "Children", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[10]<=0:
							# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[5]>1:
								return 'False'
							elif obj[5]<=1:
								# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[0]<=0:
									return 'False'
								elif obj[0]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[10]>0:
							return 'True'
						else: return 'True'
					elif obj[3]<=55:
						# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[12]>2:
							return 'True'
						elif obj[12]<=2:
							# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]<=0:
								return 'False'
							elif obj[0]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[15]>2.0:
					return 'True'
				else: return 'True'
			elif obj[9]>1:
				return 'False'
			else: return 'False'
		elif obj[2]>1:
			return 'False'
		else: return 'False'
	elif obj[16]<=1.0:
		return 'True'
	else: return 'True'

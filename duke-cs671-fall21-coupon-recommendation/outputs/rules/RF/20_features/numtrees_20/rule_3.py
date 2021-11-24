def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Coffeehouse", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[15]<=1.0:
		# {"feature": "Age", "instances": 26, "metric_value": 0.8905, "depth": 2}
		if obj[8]<=4:
			# {"feature": "Education", "instances": 20, "metric_value": 0.971, "depth": 3}
			if obj[11]<=2:
				# {"feature": "Coupon", "instances": 16, "metric_value": 1.0, "depth": 4}
				if obj[5]>1:
					# {"feature": "Occupation", "instances": 14, "metric_value": 0.9852, "depth": 5}
					if obj[12]>5:
						# {"feature": "Restaurantlessthan20", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[16]>2.0:
							# {"feature": "Driving_to", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[0]>0:
								# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[2]<=0:
									return 'True'
								elif obj[2]>0:
									return 'False'
								else: return 'False'
							elif obj[0]<=0:
								return 'False'
							else: return 'False'
						elif obj[16]<=2.0:
							return 'True'
						else: return 'True'
					elif obj[12]<=5:
						# {"feature": "Coupon_validity", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[6]>0:
							return 'False'
						elif obj[6]<=0:
							# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[0]<=0:
								return 'True'
							elif obj[0]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				elif obj[5]<=1:
					return 'False'
				else: return 'False'
			elif obj[11]>2:
				return 'False'
			else: return 'False'
		elif obj[8]>4:
			return 'False'
		else: return 'False'
	elif obj[15]>1.0:
		# {"feature": "Coupon", "instances": 25, "metric_value": 0.9044, "depth": 2}
		if obj[5]>1:
			# {"feature": "Driving_to", "instances": 16, "metric_value": 0.5436, "depth": 3}
			if obj[0]<=0:
				return 'True'
			elif obj[0]>0:
				# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[19]<=2:
					return 'False'
				elif obj[19]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[5]<=1:
			# {"feature": "Maritalstatus", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[9]<=0:
				return 'False'
			elif obj[9]>0:
				# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[4]>0:
					return 'True'
				elif obj[4]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	else: return 'True'

def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Age", "instances": 41, "metric_value": 0.9474, "depth": 1}
	if obj[8]<=6:
		# {"feature": "Time", "instances": 38, "metric_value": 0.8997, "depth": 2}
		if obj[4]<=2:
			# {"feature": "Coupon", "instances": 29, "metric_value": 0.9784, "depth": 3}
			if obj[5]>1:
				# {"feature": "Carryaway", "instances": 21, "metric_value": 0.8631, "depth": 4}
				if obj[16]<=2.0:
					# {"feature": "Distance", "instances": 11, "metric_value": 0.4395, "depth": 5}
					if obj[20]<=2:
						return 'True'
					elif obj[20]>2:
						return 'False'
					else: return 'False'
				elif obj[16]>2.0:
					# {"feature": "Coffeehouse", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[15]>0.0:
						# {"feature": "Coupon_validity", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[6]<=0:
							return 'True'
						elif obj[6]>0:
							# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[9]<=1:
								return 'False'
							elif obj[9]>1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[15]<=0.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[5]<=1:
				# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[15]<=1.0:
					return 'False'
				elif obj[15]>1.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[4]>2:
			return 'True'
		else: return 'True'
	elif obj[8]>6:
		return 'False'
	else: return 'False'

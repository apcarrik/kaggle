def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Restaurantlessthan20", "instances": 41, "metric_value": 0.9789, "depth": 1}
	if obj[17]>1.0:
		# {"feature": "Carryaway", "instances": 37, "metric_value": 0.9353, "depth": 2}
		if obj[16]>1.0:
			# {"feature": "Occupation", "instances": 31, "metric_value": 0.8238, "depth": 3}
			if obj[12]<=18:
				# {"feature": "Maritalstatus", "instances": 29, "metric_value": 0.7355, "depth": 4}
				if obj[9]>0:
					# {"feature": "Distance", "instances": 16, "metric_value": 0.3373, "depth": 5}
					if obj[20]<=2:
						return 'True'
					elif obj[20]>2:
						# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]>0:
							return 'False'
						elif obj[5]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[9]<=0:
					# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.9612, "depth": 5}
					if obj[15]>0.0:
						# {"feature": "Gender", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[7]<=0:
							return 'True'
						elif obj[7]>0:
							# {"feature": "Coupon_validity", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[6]<=0:
								return 'False'
							elif obj[6]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[15]<=0.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[12]>18:
				return 'False'
			else: return 'False'
		elif obj[16]<=1.0:
			# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[7]>0:
				return 'False'
			elif obj[7]<=0:
				# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]<=0:
					return 'False'
				elif obj[0]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[17]<=1.0:
		return 'False'
	else: return 'False'

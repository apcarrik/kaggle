def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Bar", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[14]<=1.0:
		# {"feature": "Passanger", "instances": 28, "metric_value": 0.9852, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Education", "instances": 22, "metric_value": 0.9024, "depth": 3}
			if obj[11]<=1:
				# {"feature": "Occupation", "instances": 15, "metric_value": 0.9968, "depth": 4}
				if obj[12]>1:
					# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.8454, "depth": 5}
					if obj[17]<=2.0:
						# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.5033, "depth": 6}
						if obj[15]<=2.0:
							return 'False'
						elif obj[15]>2.0:
							# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]>1:
								return 'False'
							elif obj[0]<=1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[17]>2.0:
						return 'True'
					else: return 'True'
				elif obj[12]<=1:
					return 'True'
				else: return 'True'
			elif obj[11]>1:
				return 'False'
			else: return 'False'
		elif obj[1]>2:
			# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[5]<=3:
				return 'True'
			elif obj[5]>3:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[14]>1.0:
		return 'True'
	else: return 'True'

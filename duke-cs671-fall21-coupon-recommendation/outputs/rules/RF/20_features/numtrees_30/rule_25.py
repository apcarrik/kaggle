def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Distance", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[19]<=2:
		# {"feature": "Age", "instances": 30, "metric_value": 0.9481, "depth": 2}
		if obj[8]>1:
			# {"feature": "Direction_same", "instances": 24, "metric_value": 0.995, "depth": 3}
			if obj[18]<=0:
				# {"feature": "Restaurantlessthan20", "instances": 20, "metric_value": 0.9928, "depth": 4}
				if obj[16]<=2.0:
					# {"feature": "Time", "instances": 13, "metric_value": 0.9612, "depth": 5}
					if obj[4]<=1:
						# {"feature": "Driving_to", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[0]<=1:
							return 'True'
						elif obj[0]>1:
							# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[9]<=0:
								return 'False'
							elif obj[9]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[4]>1:
						# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[5]<=3:
							return 'False'
						elif obj[5]>3:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[16]>2.0:
					# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[4]<=1:
						return 'False'
					elif obj[4]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[18]>0:
				return 'True'
			else: return 'True'
		elif obj[8]<=1:
			return 'True'
		else: return 'True'
	elif obj[19]>2:
		return 'False'
	else: return 'False'

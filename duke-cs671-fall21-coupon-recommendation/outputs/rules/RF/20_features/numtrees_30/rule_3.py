def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Age", "instances": 23, "metric_value": 0.9656, "depth": 2}
		if obj[8]<=4:
			# {"feature": "Children", "instances": 20, "metric_value": 0.8813, "depth": 3}
			if obj[10]<=0:
				# {"feature": "Occupation", "instances": 13, "metric_value": 0.9957, "depth": 4}
				if obj[12]>3:
					# {"feature": "Driving_to", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[0]>0:
						return 'False'
					elif obj[0]<=0:
						# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[4]>2:
							return 'False'
						elif obj[4]<=2:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[12]<=3:
					return 'True'
				else: return 'True'
			elif obj[10]>0:
				return 'False'
			else: return 'False'
		elif obj[8]>4:
			return 'True'
		else: return 'True'
	elif obj[1]>2:
		# {"feature": "Weather", "instances": 11, "metric_value": 0.4395, "depth": 2}
		if obj[2]<=0:
			return 'True'
		elif obj[2]>0:
			return 'False'
		else: return 'False'
	else: return 'True'

def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Driving_to", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[0]<=0:
		# {"feature": "Education", "instances": 24, "metric_value": 0.9183, "depth": 2}
		if obj[11]>1:
			# {"feature": "Age", "instances": 12, "metric_value": 0.4138, "depth": 3}
			if obj[8]<=4:
				return 'True'
			elif obj[8]>4:
				# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[9]<=0:
					return 'True'
				elif obj[9]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[11]<=1:
			# {"feature": "Occupation", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[12]<=10:
				# {"feature": "Coupon_validity", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[6]>0:
					# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[17]<=1.0:
						return 'False'
					elif obj[17]>1.0:
						return 'True'
					else: return 'True'
				elif obj[6]<=0:
					return 'True'
				else: return 'True'
			elif obj[12]>10:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]>0:
		# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[15]<=2.0:
			return 'False'
		elif obj[15]>2.0:
			# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[4]<=0:
				return 'True'
			elif obj[4]>0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'

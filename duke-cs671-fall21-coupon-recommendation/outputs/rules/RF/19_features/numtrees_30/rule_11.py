def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Weather", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[1]<=0:
		# {"feature": "Age", "instances": 25, "metric_value": 0.7219, "depth": 2}
		if obj[7]>1:
			# {"feature": "Education", "instances": 17, "metric_value": 0.874, "depth": 3}
			if obj[10]<=2:
				# {"feature": "Occupation", "instances": 10, "metric_value": 1.0, "depth": 4}
				if obj[11]<=6:
					# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[0]<=2:
						return 'False'
					elif obj[0]>2:
						return 'True'
					else: return 'True'
				elif obj[11]>6:
					# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[17]<=0:
						return 'True'
					elif obj[17]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[10]>2:
				return 'True'
			else: return 'True'
		elif obj[7]<=1:
			return 'True'
		else: return 'True'
	elif obj[1]>0:
		# {"feature": "Coupon", "instances": 9, "metric_value": 0.7642, "depth": 2}
		if obj[4]<=3:
			return 'False'
		elif obj[4]>3:
			# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[6]<=0:
				return 'True'
			elif obj[6]>0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'

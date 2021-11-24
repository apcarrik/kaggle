def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[12]>6:
		# {"feature": "Coffeehouse", "instances": 20, "metric_value": 0.971, "depth": 2}
		if obj[15]<=2.0:
			# {"feature": "Income", "instances": 16, "metric_value": 0.8113, "depth": 3}
			if obj[13]<=4:
				# {"feature": "Coupon_validity", "instances": 12, "metric_value": 0.4138, "depth": 4}
				if obj[6]>0:
					return 'False'
				elif obj[6]<=0:
					# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[5]<=1:
						return 'False'
					elif obj[5]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[13]>4:
				# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[15]>2.0:
			return 'True'
		else: return 'True'
	elif obj[12]<=6:
		# {"feature": "Children", "instances": 14, "metric_value": 0.5917, "depth": 2}
		if obj[10]<=0:
			return 'True'
		elif obj[10]>0:
			return 'False'
		else: return 'False'
	else: return 'True'

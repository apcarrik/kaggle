def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Distance", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[17]>1:
		# {"feature": "Coupon", "instances": 22, "metric_value": 0.9024, "depth": 2}
		if obj[3]>1:
			# {"feature": "Education", "instances": 17, "metric_value": 0.9774, "depth": 3}
			if obj[9]>0:
				# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.684, "depth": 4}
				if obj[15]>0.0:
					return 'False'
				elif obj[15]<=0.0:
					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]>0:
						return 'True'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[9]<=0:
				# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[10]<=10:
					return 'True'
				elif obj[10]>10:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[3]<=1:
			return 'False'
		else: return 'False'
	elif obj[17]<=1:
		# {"feature": "Time", "instances": 12, "metric_value": 0.4138, "depth": 2}
		if obj[2]<=2:
			return 'True'
		elif obj[2]>2:
			return 'False'
		else: return 'False'
	else: return 'True'

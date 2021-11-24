def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[10]>5:
		# {"feature": "Weather", "instances": 15, "metric_value": 0.9968, "depth": 2}
		if obj[1]<=0:
			# {"feature": "Gender", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[5]<=0:
				# {"feature": "Maritalstatus", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[7]>0:
					# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[0]<=2:
						return 'True'
					elif obj[0]>2:
						return 'False'
					else: return 'False'
				elif obj[7]<=0:
					return 'False'
				else: return 'False'
			elif obj[5]>0:
				return 'True'
			else: return 'True'
		elif obj[1]>0:
			return 'False'
		else: return 'False'
	elif obj[10]<=5:
		return 'True'
	else: return 'True'

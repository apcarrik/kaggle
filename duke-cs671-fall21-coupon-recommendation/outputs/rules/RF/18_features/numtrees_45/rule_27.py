def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Age", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[6]>0:
		# {"feature": "Occupation", "instances": 17, "metric_value": 0.9975, "depth": 2}
		if obj[10]<=9:
			# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[13]>0.0:
				# {"feature": "Education", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[9]<=2:
					return 'True'
				elif obj[9]>2:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]>1:
						return 'True'
					elif obj[0]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[13]<=0.0:
				# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[2]<=3:
					return 'False'
				elif obj[2]>3:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[10]>9:
			return 'False'
		else: return 'False'
	elif obj[6]<=0:
		return 'True'
	else: return 'True'

def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Bar", "instances": 16, "metric_value": 1.0, "depth": 2}
		if obj[13]>0.0:
			# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[14]<=3.0:
				# {"feature": "Coupon_validity", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[5]<=0:
					return 'True'
				elif obj[5]>0:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[10]<=0:
						return 'False'
					elif obj[10]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[14]>3.0:
				return 'False'
			else: return 'False'
		elif obj[13]<=0.0:
			return 'False'
		else: return 'False'
	elif obj[0]>1:
		return 'True'
	else: return 'True'

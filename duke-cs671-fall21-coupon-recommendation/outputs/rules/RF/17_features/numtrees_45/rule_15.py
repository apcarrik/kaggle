def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Occupation", "instances": 15, "metric_value": 0.9968, "depth": 2}
		if obj[10]<=12:
			# {"feature": "Coupon", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[3]<=2:
				# {"feature": "Gender", "instances": 8, "metric_value": 1.0, "depth": 4}
				if obj[5]<=0:
					# {"feature": "Maritalstatus", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[7]>0:
						return 'True'
					elif obj[7]<=0:
						return 'False'
					else: return 'False'
				elif obj[5]>0:
					return 'False'
				else: return 'False'
			elif obj[3]>2:
				return 'False'
			else: return 'False'
		elif obj[10]>12:
			return 'True'
		else: return 'True'
	elif obj[0]>1:
		return 'True'
	else: return 'True'

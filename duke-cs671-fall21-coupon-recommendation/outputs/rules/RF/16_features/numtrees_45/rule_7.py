def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[3]>1:
		# {"feature": "Passanger", "instances": 18, "metric_value": 0.9183, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Weather", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[1]<=0:
				# {"feature": "Age", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[6]>2:
					return 'True'
				elif obj[6]<=2:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[8]<=0:
						return 'False'
					elif obj[8]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[1]>0:
				return 'False'
			else: return 'False'
		elif obj[0]>2:
			# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[9]<=9:
				return 'True'
			elif obj[9]>9:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[3]<=1:
		return 'False'
	else: return 'False'

def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[3]>0:
		# {"feature": "Children", "instances": 20, "metric_value": 0.8813, "depth": 2}
		if obj[8]<=0:
			# {"feature": "Bar", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[12]>0.0:
				return 'True'
			elif obj[12]<=0.0:
				# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[13]<=1.0:
					return 'True'
				elif obj[13]>1.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[8]>0:
			# {"feature": "Weather", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[1]<=0:
				# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[0]<=2:
					return 'False'
				elif obj[0]>2:
					# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[6]<=6:
						return 'True'
					elif obj[6]>6:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[1]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[3]<=0:
		return 'False'
	else: return 'False'

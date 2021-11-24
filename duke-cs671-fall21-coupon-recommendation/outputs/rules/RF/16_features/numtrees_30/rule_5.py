def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Coupon_validity", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[4]>0:
		# {"feature": "Occupation", "instances": 21, "metric_value": 0.7919, "depth": 2}
		if obj[9]>5:
			# {"feature": "Education", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[8]>0:
				# {"feature": "Bar", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[11]<=1.0:
					return 'False'
				elif obj[11]>1.0:
					return 'True'
				else: return 'True'
			elif obj[8]<=0:
				# {"feature": "Income", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[10]<=6:
					return 'True'
				elif obj[10]>6:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[9]<=5:
			return 'False'
		else: return 'False'
	elif obj[4]<=0:
		# {"feature": "Coupon", "instances": 13, "metric_value": 0.7793, "depth": 2}
		if obj[3]>0:
			# {"feature": "Bar", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[11]<=2.0:
				return 'True'
			elif obj[11]>2.0:
				return 'False'
			else: return 'False'
		elif obj[3]<=0:
			return 'False'
		else: return 'False'
	else: return 'True'

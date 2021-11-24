def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Income", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[9]>1:
		# {"feature": "Occupation", "instances": 19, "metric_value": 0.9495, "depth": 2}
		if obj[8]>9:
			# {"feature": "Passanger", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[2]>0:
					return 'False'
				elif obj[2]<=0:
					# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]>0:
						return 'False'
					elif obj[4]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[0]>1:
				# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[2]>2:
					return 'True'
				elif obj[2]<=2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[8]<=9:
			# {"feature": "Age", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[5]<=4:
				return 'True'
			elif obj[5]>4:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[9]<=1:
		return 'False'
	else: return 'False'

def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[2]>2:
		# {"feature": "Coupon_validity", "instances": 18, "metric_value": 0.65, "depth": 2}
		if obj[3]<=0:
			return 'True'
		elif obj[3]>0:
			# {"feature": "Occupation", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[8]>6:
				return 'True'
			elif obj[8]<=6:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[2]<=2:
		# {"feature": "Income", "instances": 16, "metric_value": 0.8113, "depth": 2}
		if obj[9]<=7:
			# {"feature": "Occupation", "instances": 14, "metric_value": 0.5917, "depth": 3}
			if obj[8]>5:
				return 'False'
			elif obj[8]<=5:
				# {"feature": "Age", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[5]>3:
					return 'True'
				elif obj[5]<=3:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[9]>7:
			return 'True'
		else: return 'True'
	else: return 'False'

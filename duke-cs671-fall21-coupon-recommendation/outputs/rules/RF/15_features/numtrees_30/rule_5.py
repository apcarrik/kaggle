def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Coffeehouse", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[11]>0.0:
		# {"feature": "Passanger", "instances": 25, "metric_value": 0.9427, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Coupon", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[2]>1:
				# {"feature": "Children", "instances": 12, "metric_value": 0.9799, "depth": 4}
				if obj[6]<=0:
					# {"feature": "Age", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[5]<=4:
						return 'True'
					elif obj[5]>4:
						return 'False'
					else: return 'False'
				elif obj[6]>0:
					# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[8]<=12:
						return 'False'
					elif obj[8]>12:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[2]<=1:
				return 'False'
			else: return 'False'
		elif obj[0]>1:
			# {"feature": "Coupon", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[2]>0:
				return 'True'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[11]<=0.0:
		# {"feature": "Age", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[5]<=3:
			return 'False'
		elif obj[5]>3:
			return 'True'
		else: return 'True'
	else: return 'False'

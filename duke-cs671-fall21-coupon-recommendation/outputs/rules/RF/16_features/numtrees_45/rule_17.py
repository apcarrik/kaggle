def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[15]<=2:
		# {"feature": "Age", "instances": 20, "metric_value": 0.8113, "depth": 2}
		if obj[6]>3:
			# {"feature": "Coupon", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[3]>0:
				return 'True'
			elif obj[3]<=0:
				# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]>1:
					return 'True'
				elif obj[2]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[6]<=3:
			# {"feature": "Time", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[2]>1:
				# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[0]>0:
					# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[8]<=2:
						return 'False'
					elif obj[8]>2:
						return 'True'
					else: return 'True'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			elif obj[2]<=1:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[15]>2:
		return 'False'
	else: return 'False'

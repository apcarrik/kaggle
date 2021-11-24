def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[12]>0.0:
		# {"feature": "Coupon", "instances": 19, "metric_value": 0.998, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Time", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Passanger", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[0]<=1:
					return 'False'
				elif obj[0]>1:
					# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]<=0:
						return 'True'
					elif obj[4]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[2]>3:
				# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[9]<=6:
					return 'True'
				elif obj[9]>6:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[3]>2:
			# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[2]>0:
				return 'True'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[12]<=0.0:
		return 'False'
	else: return 'False'

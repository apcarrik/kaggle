def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[15]<=2:
		# {"feature": "Coupon_validity", "instances": 20, "metric_value": 1.0, "depth": 2}
		if obj[4]>0:
			# {"feature": "Occupation", "instances": 11, "metric_value": 0.8454, "depth": 3}
			if obj[9]<=9:
				return 'False'
			elif obj[9]>9:
				# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[0]>1:
					return 'True'
				elif obj[0]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[4]<=0:
			# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.7642, "depth": 3}
			if obj[12]>0.0:
				# {"feature": "Education", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[8]>0:
					return 'True'
				elif obj[8]<=0:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						return 'False'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[12]<=0.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[15]>2:
		return 'False'
	else: return 'False'

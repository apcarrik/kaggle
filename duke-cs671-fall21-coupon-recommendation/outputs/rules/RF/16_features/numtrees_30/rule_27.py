def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[9]<=6:
		# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.9495, "depth": 2}
		if obj[13]<=2.0:
			# {"feature": "Coupon_validity", "instances": 17, "metric_value": 0.874, "depth": 3}
			if obj[4]<=0:
				# {"feature": "Coupon", "instances": 10, "metric_value": 1.0, "depth": 4}
				if obj[3]<=0:
					# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[0]>0:
						return 'False'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				elif obj[3]>0:
					return 'True'
				else: return 'True'
			elif obj[4]>0:
				return 'False'
			else: return 'False'
		elif obj[13]>2.0:
			return 'True'
		else: return 'True'
	elif obj[9]>6:
		# {"feature": "Passanger", "instances": 15, "metric_value": 0.7219, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Coupon_validity", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[4]>0:
				# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3]>0:
					return 'False'
				elif obj[3]<=0:
					return 'True'
				else: return 'True'
			elif obj[4]<=0:
				return 'True'
			else: return 'True'
		elif obj[0]>1:
			return 'True'
		else: return 'True'
	else: return 'True'
